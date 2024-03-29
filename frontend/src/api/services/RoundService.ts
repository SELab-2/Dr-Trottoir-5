import {
  Body, DELETE,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  Path, POST, PATCH
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import Building from "@/api/models/Building";
import Round from "@/api/models/Round";
import {RoundWrapper} from "@/api/wrappers/RoundWrapper";

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
   * Get all buildings for a syndicus
   */
  @GET("/ronde/building/syndicus")
  getBuildingsForSyndicus(): EchoPromise<[Building]> {
    return {} as EchoPromise<[Building]>;
  }

  /**
   * Create new round
   */
  @POST("/ronde/")
  createRound(@Body() body: RoundWrapper): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Get a list of all the rounds
   */
  @GET("/ronde/")
  getRounds() : EchoPromise<Array<Round>> {
    return {} as EchoPromise<Array<Round>>
  }

  /**
   * Delete round
   */
  @DELETE('/ronde/{id}')
  deleteRoundById(@Path('id') id: number): EchoPromise<void> {
    return {} as EchoPromise<void>
  }

  /**
   * Get round by ID
   */
  @GET('/ronde/{id}/')
  getRoundById(@Path('id') id: number): EchoPromise<Round> {
    return {} as EchoPromise<Round>
  }

  /**
   * Update round by ID
   */
  @PATCH('/ronde/{id}/')
  updateRoundById(@Path('id') id: number, @Body() body: RoundWrapper): EchoPromise<Round> {
    return {} as EchoPromise<Round>
  }

  /**
   * Reset the UUID for a building
   */
  @GET('/ronde/building/uuid/{id}/reset/')
  resetBuilding(@Path('id') id: string): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  /**
   * Get a building by its UUID
   */
  @GET('/ronde/building/uuid/{id}/')
  getBuildingByUUID(@Path('id') id: string): EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(RoundService);
