# DjangoTweetAppBackend
Its a django back end project for my android application GettingTweetsApp in which I have used 'tweepy' library for 
getting list of status object of the latest user_timeline of a twitter user and extract json response from those status objects 
and passing the json response as a http response to the client in addition to this I have use pyrebase library for pushing the json response 
into the firebse database.

Requests should be made like:
http://localhost:8000/tweets/@username/

Sample Responses are like (Json response of most recent user_timeline post) :

{
  "created_at": "Thu May 31 06:40:11 +0000 2018",
  "id": 1002077262580240400,
  "id_str": "1002077262580240384",
  "text": "N this is my childhood frnd Iqbal, as a teen he was my bank, I still owe him 2011rs . thnk God he did not take inte… https://t.co/omid0XGfjG",
  "truncated": true,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https://t.co/omid0XGfjG",
        "expanded_url": "https://twitter.com/i/web/status/1002077262580240384",
        "display_url": "twitter.com/i/web/status/1…",
        "indices": [
          117,
          140
        ]
      }
    ]
  },
  "source": "Twitter for iPhone",
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "in_reply_to_screen_name": null,
  "user": {
    "id": 132385468,
    "id_str": "132385468",
    "name": "Salman Khan",
    "screen_name": "BeingSalmanKhan",
    "location": "MUMBAI",
    "description": "Film actor, artist, painter, humanitarian",
    "url": null,
    "entities": {
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 33582925,
    "friends_count": 22,
    "listed_count": 29024,
    "created_at": "Tue Apr 13 02:56:21 +0000 2010",
    "favourites_count": 0,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": false,
    "verified": true,
    "statuses_count": 42369,
    "lang": "en",
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "C0DEED",
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http://pbs.twimg.com/profile_images/838562307/IMG00882-20100416-0034_normal.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/838562307/IMG00882-20100416-0034_normal.jpg",
    "profile_link_color": "1DA1F2",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "has_extended_profile": false,
    "default_profile": true,
    "default_profile_image": false,
    "following": true,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 3404,
  "favorite_count": 30465,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "lang": "en"
}


