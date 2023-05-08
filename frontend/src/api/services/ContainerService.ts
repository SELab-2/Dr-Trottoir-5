import {
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  Query
} from '@/api/EchoFetch'
import config from '@/config'
import { AuthInterceptor } from '@/api/interceptors/AuthInterceptor'

class ContainerService extends EchoService {
  /**
   * Get a day planning.
   */
  @GET('/containers/')
  get (@Query('building') building: string,
      @Query('year') year: number,
      @Query('week') week: number): EchoPromise<any> {
    return {} as EchoPromise<any>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(ContainerService)
