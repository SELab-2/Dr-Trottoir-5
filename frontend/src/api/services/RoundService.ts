import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  Path, POST
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import Building from "@/api/models/Building";
import {RoundWrapper} from "@/api/wrappers/RoundWrapper";
import Round from "@/api/models/Round";

class RoundService extends EchoService {
  /**
   * Get a building by id
   */
  @GET("/ronde/building/{id}")
  getBuilding(@Path('id') id: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>;
  }

  /**
   * Get all locations
   */
  @GET("/ronde/locatie")
  getLocations(): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Get all buildings
   */
  @GET("/ronde/building")
  getBuildings(): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Create new round
   */
  @POST("/ronde/")
  createRound(@Body() body: RoundWrapper): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  @GET("/ronde/")
  getRondes(): EchoPromise<Round> {
    return {} as EchoPromise<Round>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(RoundService);
