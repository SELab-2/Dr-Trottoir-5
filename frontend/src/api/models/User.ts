import { UserRole } from '@/api/models/UserRole'

export default class User {
  id: number;
  first_name: string;
  last_name: string;
  date_joined: string;
  phone_nr: string;
  role: UserRole;
  email: string;
}
