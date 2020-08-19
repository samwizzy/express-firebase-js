curl -X POST -H "Authorization: key=AAAAXIv_BNQ:APA91bFFJbIKI-cucebrtwAIgvGM6d8g7WuaMiJ_ygzb_dJyiv1o80vo50j1EqeAMOzcEsKdgILirnmJvX7hUEFappsridJTmV0AKrRXIOPiU57bDfzr8Wf4s4SokOwHtUpGK9cdISIE
" -H "Content-Type: application/json" -d '{
    "notification": {
      "title": "Portugal vs. Denmark",
      "body": "5 to 1",
      "icon": "https://kadick-admin.netlify.app/assets/images/logos/kadick.svg",
      "click_action": "http://localhost:8080"
    },
    "to": "e2hwpqyMe1SHM8C_Xwg1VV:APA91bGsngBizabnWA_H6snKiU-ujNlEAKFukQvxjoxjRZevGlXh_eEk0jAC9gaDM3QUNaAP3o7ljS7g0kBD1cqOBSgHlixu8yETFff9W49CjCkEwqR1QlyWOdHC3Qd6cyLip2ejmFOw"
  }' "https://fcm.googleapis.com/fcm/send"



  curl -X POST -H "Authorization: key=AAAAXIv_BNQ:APA91bFFJbIKI-cucebrtwAIgvGM6d8g7WuaMiJ_ygzb_dJyiv1o80vo50j1EqeAMOzcEsKdgILirnmJvX7hUEFappsridJTmV0AKrRXIOPiU57bDfzr8Wf4s4SokOwHtUpGK9cdISIE
  " -H "Content-Type: application/json" -d '{
  "message": {
    "notification": {
      "title": "FCM Message",
      "body": "This is a message from FCM"
    },
    "webpush": {
      "headers": {
        "Urgency": "high"
      },
      "notification": {
        "body": "This is a message from FCM to web",
        "requireInteraction": "true",
        "badge": "/badge-icon.png"
      }
    }
  },
  "token": "e2hwpqyMe1SHM8C_Xwg1VV:APA91bGsngBizabnWA_H6snKiU-ujNlEAKFukQvxjoxjRZevGlXh_eEk0jAC9gaDM3QUNaAP3o7ljS7g0kBD1cqOBSgHlixu8yETFff9W49CjCkEwqR1QlyWOdHC3Qd6cyLip2ejmFOw"
  }
}' "https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send"
  