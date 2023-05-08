import Vue from 'vue'
import { Router } from 'vue-router'

export class RouterUtil {
  /**
   * Reload the current route.
   * @param router Instance of the current Vue router
   */

  static reload (router: Router) {
    const location = router.currentRoute.value.path

    router.replace('/')

    Vue.nextTick(() => router.push(location))
  }
}
