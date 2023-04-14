import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST,
  FormMultipart,
  FormField, GET, Path, DELETE, PATCH
} from "@/api/EchoFetch";
import Building from "@/api/models/Building";import config from "@/config";
import {InputFields} from "@/types/fields/InputFields";

class BuildingService extends EchoService {

  /**
   * Create a new building
   */
  @POST('/ronde/building/')
  createBuilding(@Body() body: InputFields): EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }

  /**
   * Get building information
   */
  @GET('/ronde/building/{id}/')
  getBuildingById(@Path('id') id: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>
  }

  /**
   * Update building information
   */
  @PATCH('/ronde/building/{id}/')
  updateBuildingById(@Path('id') id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  /**
   * Delete building
   */
  @DELETE('/ronde/building/{id}')
  deleteBuildingById(@Path('id') id: number): EchoPromise<void> {
    return {} as EchoPromise<void>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(BuildingService);
