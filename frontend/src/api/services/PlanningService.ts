import {
  Body,
  DELETE,
  EchoPromise,
  EchoService,
  EchoServiceBuilder, FormField, FormMultipart,
  GET, PATCH, Path, POST, PUT,
  Query
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import DayPlanning from "@/api/models/Planning";
import BuildingInfo from "@/api/models/BuildingInfo";
import {PlanningStatusWrapper} from "@/api/wrappers/PlanningWrappers";

class PlanningService extends EchoService {
  /**
   * Get a day planning
   */
  @GET("/planning/dagplanning/")
  get(@Query('student') student: string,
      @Query('date') date: string): EchoPromise<DayPlanning> {
    return {} as EchoPromise<DayPlanning>;
  }

  /**
   * Get a day planning by id
   */
  @GET("/planning/dagplanning/{id}/")
  getPlanning(@Path('id') id: number): EchoPromise<DayPlanning> {
    return {} as EchoPromise<DayPlanning>;
  }

  /**
   * Get building info for a day planning
   */
  @GET("/planning/infoperbuilding/")
  getInfo(@Query('dagPlanning') dagPlanning: number): EchoPromise<BuildingInfo> {
    return {} as EchoPromise<BuildingInfo>;
  }

  /**
   * Get student images for building info
   */
  @GET("/planning/buildingpicture/")
  getPictures(@Query('infoPerBuilding') infoPerBuilding: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Get student image by id
   */
  @GET("/planning/buildingpicture/{id}/")
  getPicture(@Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Delete a building picture
   */
  @DELETE("/planning/buildingpicture/{id}/")
  deletePicture(@Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Post building picture
   */
  @POST("/planning/buildingpicture/")
  @FormMultipart()
  uploadPicture(
    @FormField("image") image: File,
    @FormField("infoPerBuilding") infoPerBuilding: number,
    @FormField("pictureType") pictureType: string,
    @FormField("time") time: string,
    @FormField("remark") remark: string
  ): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Update building picture
   */
  @PUT("/planning/buildingpicture/{id}/")
  @FormMultipart()
  updatePicture(
    @Path('id') id: number,
    @FormField("image") image: File,
    @FormField("infoPerBuilding") infoPerBuilding: number,
    @FormField("pictureType") pictureType: string,
    @FormField("time") time: string,
    @FormField("remark") remark: string
  ): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Partly update building picture
   */
  @PATCH("/planning/buildingpicture/{id}/")
  @FormMultipart()
  patchPicture(
    @Path('id') id: number,
    @FormField("infoPerBuilding") infoPerBuilding: number,
    @FormField("pictureType") pictureType: string,
    @FormField("time") time: string,
    @FormField("remark") remark: string
  ): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Update planning status
   */
  @PATCH("/planning/dagplanning/{id}/")
  updatePlanningStatus(@Path('id') id: number, @Body() body: PlanningStatusWrapper) {
    return {} as EchoPromise<any>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(PlanningService);
