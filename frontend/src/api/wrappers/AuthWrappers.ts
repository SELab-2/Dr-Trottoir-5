export class AuthRegisterWrapper {
  public email: string;
  public password: string;
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
  public new_password: string;
  public otp: string;

  constructor(email: string, new_password: string, otp: string) {
    this.email = email
    this.new_password = new_password
    this.otp = otp
  }
}
