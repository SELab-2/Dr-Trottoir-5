import router from '@/router'
/* eslint-disable */

function requestWithBody (url, method, body, headers = {}) {
  headers.Accept = 'application/json'
  headers['Content-Type'] = 'application/json'
  return fetch(url, {
    method: method,
    headers: headers,
    body: JSON.stringify(body)
  }).then(r => r.json())
    .then(data => { return data })
}

function getRequest (url, headers) {
  return fetch(url, {
    method: 'GET',
    headers: headers
  }).then(r => r.json())
    .then(data => { return data })
}

export async function request(url, method, headers = {}, body = {}) {
  /*
    Executes the requested http method on the given url with optional headers and body.
    It adds the access token to the request if an access token is available, otherwise it gets
    a new one with the refresh token or redirects to the login page.
  */

  let access_token = $cookies.get('access_token')
  let refresh_token = $cookies.get('refresh_token')

  if(typeof refresh_token !== 'string' || typeof access_token !== 'string') { // user is not logged in
    return await router.push({path: '/login'})
  }

  // do the request
  headers['Authorization'] = `Bearer ${access_token}`
  let result
  if(method === 'GET') {
    result = await getRequest(url, headers)
  } else {
    result = await requestWithBody(url, method, body, headers)
  }

  if (result.code === 'token_not_valid') {  // access token is expired or invalid

    // see if you can refresh with the refresh token
    result = await requestWithBody('/api/refresh/', 'POST', {'refresh': refresh_token})

    if(result.code === 'token_not_valid') {  // refresh token is expired or invalid
      return await router.push({path: '/login'})  // need to login again
    }

    // set new tokens in cookies
    $cookies.set("access_token", result.access)
    $cookies.set("refresh_token", result.refresh)

    // redo the request with valid access token
    headers['Authorization'] = `Bearer ${result.access}`
    if(method === 'GET') {
      result = await getRequest(url, headers)
    } else {
      result = await requestWithBody(url, 'POST', body, headers)
    }
  }
  return result
}


export async function loginUser(email, password, return_path) {
  /*
    Logs the user in and redirects back to the original url or to the home page.
  */
  if(email === '') return { message: 'Email is verplicht.' }
  if(password === '') return { message: 'Wachtwoord is verplicht.' }
  const data = {
      'email': email,
      'password': password
  }
  const tokens = await requestWithBody('/api/login/', 'POST', data)

  if ('access' in tokens) { // login succeeded
    $cookies.set('access_token', tokens.access)
    $cookies.set('refresh_token', tokens.refresh)
    return await router.push({ path: return_path })
  }
  return { message: 'Email of wachtwoord is incorrect.' }
}
