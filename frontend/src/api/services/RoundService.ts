import {
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  Path
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import Building from "@/api/models/Building";

class RoundService extends EchoService {
  /**
   * Get a building by id
   */
  @GET("/ronde/building/{id}")
  getBuilding(@Path('id') id: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(RoundService);
