import Round from "@/api/models/Round";

export default class DayPlanning {
  id: number;
  student: number;
  date: string;
  ronde: Round;
  weekPlanning: number;
}
