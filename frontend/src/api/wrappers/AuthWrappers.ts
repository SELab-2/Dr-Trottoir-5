export class AuthRegisterWrapper {
  public email: string;
  public password: string;
  public password2: string;
  public first_name: string;
  public last_name: string;
  public phone_nr: string;

  constructor(email: string, password: string, password2: string, first_name: string, last_name: string, phone_nr: string) {
    this.email = email;
    this.password = password;
    this.password2 = password2;
    this.first_name = first_name;
    this.last_name = last_name;
    this.phone_nr = phone_nr;
  }
}

export class AuthLoginWrapper {
  public email: string;
  public password: string;
}

export class AuthForgotWrapper {
  public email: string;
  constructor(email: string) {
    this.email = email
  }
}

export class AuthResetWrapper {
  public email: string;
  public password: string;
  public password2: string;
  public otp: string;

  constructor(email: string, password: string, password2: string, otp: string) {
    this.email = email
    this.password = password
    this.password2 = password2
    this.otp = otp
  }
}
