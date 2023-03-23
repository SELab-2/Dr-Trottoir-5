/* eslint-disable */
import router from "@/router"
import {ref} from "vue";

function request_with_body(url, method, body, headers={}) {
  headers['Accept'] = 'application/json'
  headers['Content-Type'] = 'application/json'
  return fetch(url, {
    method: method,
    headers: headers,
    body: JSON.stringify(body)
  }).then(r => r.json())
    .then(data => { return data })
}

function get_request(url, headers) {
  return fetch(url, {
    method: 'POST',
    headers: headers,
  }).then(r => r.json())
    .then(data => { return data })
}

export async function request(url, method, headers={}, body={}) {
  let access_token = $cookies.get('access_token')
  let refresh_token = $cookies.get('refresh_token')

  if(refresh_token === 'undefined' || access_token === 'undefined') { // user is not logged in
    return await router.push({name: 'login'})
  }

  headers['Authorization'] = `Bearer ${access_token}`
  let result
  if(method === 'GET') {
    result = await get_request(url, headers)
  } else {
    result = await request_with_body(url, headers, body)
  }

  if (result.code === 'token_not_valid') {  // access token is invalid or expired

    // see if you can refresh access token
    result = await request_with_body('/api/refresh/', 'POST', {'refresh': refresh_token})

    if(result.code === 'token_not_valid') {  // refresh token is expired or invalid
      return await router.push({path: '/login'})
    }

    // set new tokens in cookies
    $cookies.set("access_token", result.access)
    $cookies.set("refresh_token", result.refresh)

    // redo the request with valid access token
    headers['Authorization'] = `Bearer ${result.access}`
    if(method === 'GET') {
      result = await get_request(url, headers)
    } else {
      result = await request_with_body(url, 'POST', body)
    }
  }
  return result
}


export async function loginUser(email, password, from_route) {
  const return_name = from_route !== null ? from_route.name : 'home'
  const data = {
      'email': email,
      'password': password
  }
  const tokens = await request_with_body('/api/login/', 'POST', data)
  $cookies.set('access_token', tokens.access)
  $cookies.set('refresh_token', tokens.refresh)
  return await router.push({name: return_name})
}
