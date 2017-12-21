var admin = require("firebase-admin");
var serviceAccount = require("C:/Program Files/nodejs/serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://iotcase-10777.firebaseio.com"
});

// This registration token comes from the client FCM SDKs.
var registrationToken = "fmHG50Y2QOA:APA91bGZ2hmVOIjULnUkXk62WEcmQXtu0l9bdaIkNVKN_l4VyTigWac_eQWEJc152zvJ14av3-Hok-FrInXTvX2Jrk2-KDY4DWuqgxq89jxpR2JmRLE_EFo2jiDUjfTRjLvAGv11ZoaM";

var payload = {
  notification: {
    title: "IoTCase",
    body: "당신의 사물함이 열려있습니다. 도난의 위험이 있으므로 확인해보시길 바랍니다."
  }
};

// Send a message to the device corresponding to the provided registration token.
admin.messaging().sendToDevice(registrationToken, payload)
  .then(function(response) {
    console.log("Successfully sent message:", response);
  })
  .catch(function(error) {
    console.log("Error sending message:", error);
  });
