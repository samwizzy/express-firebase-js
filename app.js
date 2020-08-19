const firebaseConfig = require('./services/firebaseConfig')
const firebase = require('firebase/app')
require('firebase/auth')
require('firebase/database')
require('@firebase/messaging')

firebase.initializeApp(firebaseConfig)
const messaging = firebase.messaging();

messaging.requestPermission()
    .then(() => {
        return messaging.getToken()
    })
    .then((token) => {
        console.log("Firebase token: ", token)
    })
    .catch((error) => {
        console.log("Error fired: ", error)
    })

messaging.onMessage((payload) => {
    console.log("onMessage: ", payload)
})

// Callback fired if Instance ID token is updated.
messaging.onTokenRefresh(() => {
    messaging.getToken().then((refreshedToken) => {
        console.log('Token refreshed: ', refreshedToken);
    }).catch((err) => {
        console.log('Unable to retrieve refreshed token: ', err);
    });
});