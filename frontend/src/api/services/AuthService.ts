import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST
} from 'echofetch'
import { ErrorHandler } from '@/api/error/ErrorHandler'
import { AuthInterceptor } from '@/api/interceptors/AuthInterceptor'
import config from '@/config'
import { store } from '../../store'
import router from '../../router'
import { AuthForgotWrapper, AuthLoginWrapper, AuthRegisterWrapper, AuthResetWrapper } from '@/api/wrappers/AuthWrappers'
import User from '@/api/models/User'

class AuthService extends EchoService {
  /**
   * Login into an account.
   * @param body User parameters to login.
   */
  @POST('/login/')
  login (@Body() body: AuthLoginWrapper): EchoPromise<User> {
    return {} as EchoPromise<User>
  }

  /**
   * Create a new user.
   * @param body User parameters for the new user.
   */
  @POST('/register/')
  register (@Body() body: AuthRegisterWrapper): EchoPromise<User> {
    return {} as EchoPromise<User>
  }

  /**
   * Send an otp.
   * @param body Email address
   */
  @POST('/forgot/')
  forgot (@Body() body: AuthForgotWrapper): EchoPromise<string> {
    return {} as EchoPromise<string>
  }

   /**
   * Reset the users password
   * @param body Email, new_password and otp
   */
  @POST('/reset/')
  reset (@Body() body: AuthResetWrapper): EchoPromise<string> {
    return {} as EchoPromise<string>
  }

  /**
   * Logout the current user.
   */
  @POST('/logout/')
  logout (): EchoPromise<string> {
    return {} as EchoPromise<string>
  }

  /**
   * Call the logout function and show the progress
   * @param goHome If the user should be send to the homepage after logging out.
   */
  async handleLogout (goHome = false) {
    // Send loading message.
    store.dispatch('snackbar/open', {
      message: 'Logging out...',
      color: 'info',
      timeout: 120 * 1000
    })

    this.logout()
      .then(async (_) => {
        // Send confirmation message.
        store.dispatch('snackbar/open', {
          message: 'U bent uitgelogd',
          color: 'success'
        })
        // Update the current user inside the store.
        store.dispatch('session/clear')
        await store.dispatch('session/fetch')

        await router.push(goHome ? { name: 'home' } : { name: 'login' })
      })
      .catch((error) => {
        ErrorHandler.handle(error, {
          style: 'SECTION',
          id: 'logout',
          displayFullpage: true
        })
      })
  }

  /**
   * Change the role of a user
   */
  @POST('/role/')
  updateRoleOfUser (@Body() body : {}) : EchoPromise<string> {
    return {} as EchoPromise<string>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(AuthService)
