package kr.ac.kumoh.s20130870.iotcase;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Environment;
import android.os.StrictMode;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

import static android.os.StrictMode.setThreadPolicy;

public class MainActivity extends AppCompatActivity {

    private String state;
    private Button onmode = null;
    private Button oncamera = null;
    private Button reload = null;
    private TextView temp = null;
    private TextView humi = null;

    private boolean isMode = false;

    private static final String DATA_PATH = Environment.getExternalStorageDirectory().getAbsolutePath() + "/SmartCase";
    private static final int MY_PERMISSIONS_REQUEST_READ_CONTACTS = 1;
    private static String[] PERMISSIONS_STORAGE = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };

    private String[] th;
    private String HOSTNAME = "192.168.0.105";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        setThreadPolicy(policy);

        init();
        connectListener();
    }

    protected void init(){
        onmode = (Button)findViewById(R.id.onmode);
        oncamera = (Button)findViewById(R.id.oncamera);
        reload = (Button)findViewById(R.id.reload);
        temp = (TextView)findViewById(R.id.temp);
        humi = (TextView)findViewById(R.id.humi);
    }

    protected void connectListener(){
        onmode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(isMode == false) {
                    SocketThread s = new SocketThread();
                    s.run();
                    onmode.setText("감시모드 끄기");
                    isMode = true;

                } else { // isMode == true
                    SocketThread s = new SocketThread();
                    s.run();
                    onmode.setText("감시모드 켜기");
                    isMode = false;
                }
            }
        });

        oncamera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!isMode) {
                    Toast.makeText(MainActivity.this, "감시모드를 키고 이용하셔야 합니다.", Toast.LENGTH_SHORT).show();
                    Log.i("check","감시모드 키지 않은 상태");
                    return;
                }
                Socket socket;
                try {
                    if (!checkExternalStorage()) {
                        Toast.makeText(MainActivity.this, "사진 가져오기 기능을 사용하실 수 없습니다.", Toast.LENGTH_SHORT).show();
                        return;
                    }

                    socket = new Socket(HOSTNAME, 12345);

                    // 출력 스트림 : 서버에 데이터를 송신
                    OutputStream out = socket.getOutputStream();

                    out.write("get".getBytes());

                    DataInputStream dis;
                    FileOutputStream fos;
                    BufferedOutputStream bos;
                    long start = System.currentTimeMillis();
                    String filename = Long.valueOf(start).toString();

                    int control = 0;

                    dis = new DataInputStream(socket.getInputStream());

                    String inDate   = new java.text.SimpleDateFormat("yyyy-MM-dd").format(new java.util.Date());
                    String inTime   = new java.text.SimpleDateFormat("HH:mm:ss").format(new java.util.Date());
                    String fname = "Sceenshot " + inDate + " "+inTime + ".png";

                    // 파일을 생성하고 파일에 대한 출력 스트림 생성
                    File f = new File(DATA_PATH,fname);
                    fos = new FileOutputStream(f);
                    bos = new BufferedOutputStream(fos);

                    // 바이트 데이터를 전송받으면서 기록
                    int len;
                    byte[] data = new byte[4096];
                    while ((len = dis.read(data)) != -1) {
                        control++;
                        if(control % 10000 == 0)
                            Log.i("check","수신중..." + control/10000);

                        bos.write(data, 0, len);
                    }
                    long end = System.currentTimeMillis();
                    Log.i( "check","Elapsed Time (seconds) : " + ( end - start )/1000.0 );

                    bos.flush();
                    bos.close(); fos.close();
                    dis.close(); out.close();
                    socket.close();

                    Toast.makeText(MainActivity.this, fname +"\r\n카메라 캡쳐 완료", Toast.LENGTH_SHORT).show();
                } catch (IOException e) {
                    e.printStackTrace();
                }

            }
        });

        reload.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!isMode) {
                    Toast.makeText(MainActivity.this, "감시모드를 키고 이용하셔야 합니다.", Toast.LENGTH_SHORT).show();
                    Log.i("check","감시모드 키지 않은 상태");
                    return;
                }
                try{
                    Socket socket = new Socket(HOSTNAME, 12345);

                    // 출력 스트림
                    // 서버에 데이터를 송신
                    OutputStream out = socket.getOutputStream();

                    // 서버에 데이터 송신
                    out.write("set".getBytes());
                    out.flush();

                    // 서버에서 보낸 데이터를 받음
                    BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    String data = in.readLine();

                    Log.i("check",data);

                    // 서버 접속 끊기
                    in.close();
                    out.close();
                    socket.close();

                    th = data.split(",");

                } catch (UnknownHostException ue) {
                    System.out.println(ue);
                    ue.printStackTrace();
                } catch (IOException ie) {
                    System.out.println(ie);
                    ie.printStackTrace();
                }

                temp.setText("온도 : " + th[0] + "℃");
                humi.setText("습도 : " + th[1] + "%");
            }
        });
    }

    boolean checkExternalStorage() {
        state = Environment.getExternalStorageState();
        // 외부메모리 상태
        if (Environment.MEDIA_MOUNTED.equals(state)) {
            // 읽기 쓰기 모두 가능
            Log.d("check", "외부메모리 읽기 쓰기 모두 가능");
            return true;
        } else if (Environment.MEDIA_MOUNTED_READ_ONLY.equals(state)){
            //읽기전용
            Log.d("check", "외부메모리 읽기만 가능");
            return false;
        } else {
            // 읽기쓰기 모두 안됨
            Log.d("check", "외부메모리 읽기쓰기 모두 안됨 : "+ state);
            return false;
        }
    }

    @Override
    protected void onStart() {
        super.onStart();

        checkExternalStorage();

        if (ContextCompat.checkSelfPermission(MainActivity.this,
                Manifest.permission.WRITE_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED) {

            // 권한 획득에 대한 설명 보여주기
            if (ActivityCompat.shouldShowRequestPermissionRationale(MainActivity.this,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE)) {
                // 사용자에게 권한 획득에 대한 설명을 보여준 후 권한 요청을 수행
            } else {
                // 권한 획득의 필요성을 설명할 필요가 없을 때는 아래 코드를
                //수행해서 권한 획득 여부를 요청한다.
                ActivityCompat.requestPermissions(MainActivity.this,
                        PERMISSIONS_STORAGE,
                        MY_PERMISSIONS_REQUEST_READ_CONTACTS);
            }
        }

        File dir = new File(DATA_PATH);
        if(!dir.exists()) {
            if(!dir.mkdir()){
                Toast.makeText(MainActivity.this, "SmartCase 폴더 생성 실패", Toast.LENGTH_SHORT).show();
                Toast.makeText(MainActivity.this, "사진 가져오기 기능을 사용하지 못합니다.", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(MainActivity.this, "SmartCase 폴더 생성 성공", Toast.LENGTH_SHORT).show();
            }
        }

        Log.i("check",DATA_PATH);
    }

    public class SocketThread extends Thread{
        @Override
        public void run() {
            try{
                Socket socket = new Socket(HOSTNAME, 12345);

                // 출력 스트림
                // 서버에 데이터를 송신
                OutputStream out = socket.getOutputStream();

                // 서버에 데이터 송신
                if(isMode == false) {
                    out.write("on".getBytes());
                    out.flush();
                } else if(isMode == true) {
                    out.write("off".getBytes());
                    out.flush();
                }

                // 서버 접속 끊기
                out.close();
                socket.close();
            } catch (UnknownHostException ue) {
                System.out.println(ue);
                ue.printStackTrace();
            } catch (IOException ie) {
                System.out.println(ie);
                ie.printStackTrace();
            }
        }
    }
}
