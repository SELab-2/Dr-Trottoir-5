import {
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  Path
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import TrashTemplate from "@/api/models/TrashTemplate";
import Container from "@/api/models/Container";
import Building from "@/api/models/Building";

class TrashTemplateService extends EchoService {
  /**
   * Get a building by id
   */
  @GET("/trashtemplates/")
  getTrashTemplates(): EchoPromise<TrashTemplate[]> {
    return {} as EchoPromise<TrashTemplate[]>;
  }

  @GET("/trashtemplates/{id}/")
  getTrashTemplate(@Path('id') id: number): EchoPromise<TrashTemplate> {
    return {} as EchoPromise<TrashTemplate>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/")
  getTrashContainersOfTemplate(@Path('id') id: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/eenmalig/")
  getTrashContainersOfTemplateEenmalig(@Path('id') id: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/{extraId}/eenmalig/")
  getTrashContainersEenmaligOfTemplateByExtraId(@Path('id') id: number, @Path('extraId') extraId: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/trashcontainers/{extraId}/")
  getTrashContainersEOfTemplateByExtraId(@Path('id') id: number, @Path('extraId') extraId: number): EchoPromise<Container[]> {
    return {} as EchoPromise<Container[]>;
  }

  @GET("/trashtemplates/{id}/buildings/")
  getBuildingsOfTemplate(@Path('id') id: number): EchoPromise<Building[]> {
    return {} as EchoPromise<Building[]>;
  }

  @GET("/trashtemplates/{id}/buildings/eenmalig/")
  getBuildingsEenmaligOfTemplate(@Path('id') id: number): EchoPromise<Building[]> {
    return {} as EchoPromise<Building[]>;
  }

  @GET("/trashtemplates/{id}/buildings/{buildingId}/")
  getBuildingOfTemplate(@Path('id') id: number, @Path('buildingId') buildingId: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>;
  }

  @GET("/trashtemplates/{id}/buildings/{buildingId}/eenmalig/")
  getBuildingEenmaligOfTemplate(@Path('id') id: number, @Path('buildingId') buildingId: number): EchoPromise<Building> {
    return {} as EchoPromise<Building>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(TrashTemplateService);
