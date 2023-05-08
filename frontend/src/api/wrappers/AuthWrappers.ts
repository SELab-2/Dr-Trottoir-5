export class AuthRegisterWrapper {
  public email: string;
  public password: string;
  public first_name: string;
  public last_name: string;
  public phone_nr: string;

  constructor (email: string, password: string, first_name: string, last_name: string, phone_nr: string) {
    this.email = email
    this.password = password
    this.first_name = first_name
    this.last_name = last_name
    this.phone_nr = phone_nr
  }
}

export class AuthLoginWrapper {
  public email: string;
  public password: string;
}

export class AuthForgotWrapper {
  public email: string;
  constructor (email: string) {
    this.email = email
  }
}

export class AuthResetWrapper {
  public email: string;
  public new_password: string;
  public otp: string;

  constructor (email: string, new_password: string, otp: string) {
    this.email = email
    this.new_password = new_password
    this.otp = otp
  }
}
