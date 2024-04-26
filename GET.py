from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_users', methods=['GET'])
def get_users():
    user = request.args.get('user')
    if user:
        headers = {
            'authority': 'www.tiktok.com',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': f'https://www.tiktok.com/@{user}',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'WebIdLastTime': '1710499238',
            'aid': '1988',
            'app_language': 'ar',
            'app_name': 'tiktok_web',
            'browser_language': 'ar-EG',
            'browser_name': 'Mozilla',
            'browser_online': 'true',
            'browser_platform': 'Linux armv81',
            'browser_version': '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'channel': 'tiktok_web',
            'cookie_enabled': 'true',
            'count': '30',
            'device_id': '7346537195026548230',
            'device_platform': 'web_pc',
            'focus_state': 'true',
            'from_page': 'user',
            'history_len': '13',
            'is_fullscreen': 'false',
            'is_page_visible': 'true',
            'maxCursor': '0',
            'minCursor': '0',
            'os': 'linux',
            'priority_region': '',
            'referer': '',
            'region': 'IQ',
            'scene': '67',
            'screen_height': '873',
            'screen_width': '393',
            'secUid': 'MS4wLjABAAAAXCXUgqpQhjrCilWQ9y0Yzk1_Nq2-wBDpy4A1QhyKyH030GNYtl0eNq13mOgDfMmI',
            'tz_name': 'Asia/Baghdad',
            'webcast_language': 'ar',
            'msToken': '9nn_Ft3jY4S9vpyQevPtV7wRwx6pWVU-e34H8WY1-8hS9ORc__X_WnFaU70JjORHxYWUiNIJJ9KduZIA3svSYWz_I3iQoVZ8KtGrIjz7lfnB8q8gJhdSE6rCKwF7F9D65unuwhGLWGqrBmCNWIpZ',
            'X-Bogus': 'DFSzswVLbVzANn49t-nvpYx3eR3G',
            '_signature': '_02B4Z6wo000013fKuxwAAIDCNPbv.GonskN3yr-AALwG95',
        }

        session = requests.Session()
        Url = 'https://www.tiktok.com/'
        res = session.get(Url)
        req = session.cookies.get_dict()
        response = session.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers).cookies.get_dict()

        token = response["msToken"]
        
        return jsonify(response)
    else:
        return jsonify({'error': 'User parameter is missing'})

if __name__ == '__main__':
    app.run(debug=True)
