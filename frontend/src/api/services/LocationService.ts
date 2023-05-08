import { Body, EchoPromise, EchoService, EchoServiceBuilder, GET, POST } from '@/api/EchoFetch'
import config from '@/config'
import Location from '@/api/models/Location'
import { InputFields } from '@/types/fields/InputFields'

class LocationService extends EchoService {
  /**
   * Get locations
   */
  @GET('/ronde/locatie/')
  getLocations () : EchoPromise<Location[]> {
    return {} as EchoPromise<Location[]>
  }

  /**
   * Add Location
   */
  @POST('/ronde/locatie/')
  createLocation (@Body() body: InputFields) : EchoPromise<Location> {
    return {} as EchoPromise<Location>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(LocationService)
