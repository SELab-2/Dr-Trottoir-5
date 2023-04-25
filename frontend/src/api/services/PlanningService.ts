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
import Round from "@/api/models/Round";

class PlanningService extends EchoService {
  /**
   * Get a day planning
   */
  @GET("/dagplanning/{year}/{week}/{day}/")
  get(@Path('year') year: number,
      @Path('week') week: number,
      @Path('day') day: number): EchoPromise<[DayPlanning]> {
    return {} as EchoPromise<[DayPlanning]>;
  }

  /**
   * Get the statuses for a planning
   */
  @GET("/dagplanning/{year}/{week}/{id}/status/")
  getStatus(@Path('year') year: number,
            @Path('week') week: number,
            @Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Get a day planning by id
   */
  @GET("/dagplanning/{id}/")
  getPlanning(@Path('id') id: number): EchoPromise<DayPlanning> {
    return {} as EchoPromise<DayPlanning>;
  }

  @GET("/studenttemplates/rondes/{year}/{week}/{day}/{location}/")
  getRounds(@Path('year') year: number,
            @Path('week') week: number,
            @Path('day') day: number,
            @Path('location') location: number): EchoPromise<[Round]> {
    return {} as EchoPromise<[Round]>;
  }

  /**
   * Get building info for a day planning
   */
  @GET("/infoperbuilding/")
  getInfo(@Query('dagPlanning') dagPlanning: number): EchoPromise<BuildingInfo> {
    return {} as EchoPromise<BuildingInfo>;
  }

  /**
   * Get student images for building info
   */
  @GET("/buildingpicture/")
  getPictures(@Query('infoPerBuilding') infoPerBuilding: number,
              @Query('year') year: number,
              @Query('week') week: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Get student image by id
   */
  @GET("/buildingpicture/{id}/")
  getPicture(@Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Delete a building picture
   */
  @DELETE("/buildingpicture/{id}/")
  deletePicture(@Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>;
  }

  /**
   * Post building picture
   */
  @POST("/buildingpicture/")
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
  @PUT("/buildingpicture/{id}/")
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
  @PATCH("/buildingpicture/{id}/")
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

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(PlanningService);
