import {
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  Query
} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import DayPlanning from "@/api/models/Planning";

class PlanningService extends EchoService {
  /**
   * Get a day planning.
   */
  @GET("/planning/dagplanning/")
  get(@Query('student') student: string,
      @Query('date') date: string): EchoPromise<DayPlanning> {
    return {} as EchoPromise<DayPlanning>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(PlanningService);
