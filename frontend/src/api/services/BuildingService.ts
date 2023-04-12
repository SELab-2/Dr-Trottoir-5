import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST,
  FormMultipart,
  FormField, GET, Path, DELETE, PATCH
} from "@/api/EchoFetch";
import Building from "@/api/models/Building";
import BuildingManual from "@/api/models/BuildingManual";
import config from "@/config";
import {BuildingManualStatus} from "@/api/models/BuildingManualStatus";
import {InputFields} from "@/types/fields/InputFields";

class BuildingService extends EchoService {
  /**
   * Add building manual
   */
  @FormMultipart()
  @POST('/ronde/building/manual/')
  createManual(@FormField('file') file: File,
               @FormField('fileType') fileType: string,
               @FormField('manualStatus') manualStatus: BuildingManualStatus): EchoPromise<BuildingManual> {
    return {} as EchoPromise<BuildingManual>
  }

  /**
   * Get building manual
   */
  @GET('/ronde/building/manual/{id}')
  getManualById(@Path('id') id: number): EchoPromise<BuildingManual> {
    return {} as EchoPromise<BuildingManual>
  }

  /**
   * Delete building manual
   */
  @DELETE('/ronde/building/manual/{id}')
  deleteManualById(@Path('id') id: number): EchoPromise<void> {
    return {} as EchoPromise<void>
  }

  /**
   * Update a building manual
   */
  @PATCH('/ronde/building/manual/{id}/')
  updateManualStatusById(@Path('id') id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  // TODO Check Error with EchoFetch no payloud
  @PATCH('/ronde/building/manual/{id}/')
  updateManualFileById(@Path('id') id: number,
                       @FormField('file') file: File,
                       @FormField('fileType') fileType: string,
                       @FormField('manualStatus') manualStatus: BuildingManualStatus): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

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
