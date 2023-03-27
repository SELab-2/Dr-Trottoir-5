import {EchoError} from "echofetch";
import {CustomErrorOptions} from "./types/CustomErrorOptions";
import {CustomErrorMessage} from "./types/CustomErrorMessage";
import {InputFields} from "@/types/fields/InputFields";
import {InputFieldError} from "@/types/fields/InputFieldError";
import router from '../../router'


const emitter = require('tiny-emitter/instance');


/**
 * List with custom error messages for certain response codes/messages
 */
const globalCustomErrors: Array<CustomErrorMessage> = [
  {
    code: "401",
    message: "Je bent niet ingelogd",
    description:
      "Je bent momenteel niet ingelogd, log in en probeer het opnieuw",
  },
  {
    code: "404",
    message: "Pagina niet gevonden",
    description:
      "We hebben deze pagina niet gevonden. De pagina bestaat niet meer of is verplaatst naar een andere locatie.",
  },

  {
    code: "500",
    message: "Interne server error",
    description:
      "We hebben problemen met de server. Probeer het later opnieuw.",
  },

  {
    code: "502",
    message: "De server is momenteel offline.",
    description:
      "We hebben problemen met de server. Probeer het later opnieuw.",
  },

  {
    code: "network_error",
    message: "Geen connectie met de server.",
    description:
      "We kunnen niet verbinden met de server om informatie op te halen. Check of je internet hebt en probeer later opnieuw.",
  },
];

export class ErrorHandler {
  /**
   * Handle an error, received from a fetch.
   * @param error
   * @param options
   * @param fields
   */
  static handle(
    error: EchoError,
    options: CustomErrorOptions,
    fields: InputFields = {}
  ) {
    // Handle field errors.
    this.handleInputFields(error, fields);

    // Handle general errors.
    this.handleGeneral(error);

    // Emit the error on the ErrorBus.
    emitter.emit("error", error, options);

    // Clear the error when navigating to a different route.
    router.afterEach(() => {
      emitter.emit("error-clear");
    });

  }

  /**
   * Handle the error for the given InputFields.
   * This will add an error to every given field with errors.
   * @param error
   * @param fields
   */
  static handleInputFields(error: EchoError, fields: InputFields) {
    // Check if the input errors are undefined.
    if (
      !error ||
      !error.response ||
      !error.response.data ||
      // @ts-ignore TODO FIX
      !error.response.data.inputErrors
    ) {
      return;
    }
    // @ts-ignore TODO FIX
    const inputErrors = error.response.data.inputErrors;

    // Set the error messages for every field.
    for (const fieldName of Object.keys(fields)) {
      const fieldValue = fields[fieldName];
      const fieldNewError = inputErrors.find(
        (inputError: InputFieldError) => inputError.field === fieldName
      );

      // Set the new error message, when available.
      if (fieldNewError) {
        fieldValue.error = fieldNewError.message;
      }

      // Otherwise set an empty error. (necessary for reset of previous error)
      else {
        fieldValue.error = "";
      }
    }
  }

  /**
   * Handle general errors.
   * This will modify the error to the first given "generalError" message
   * @param error
   */
  static handleGeneral(error: EchoError) {
    // Check if the general errors are undefined.
    if (
      !error ||
      !error.response ||
      !error.response.data ||
      // @ts-ignore TODO FIX
      !error.response.data.generalErrors
    ) {
      return;
    }
    // @ts-ignore TODO FIX
    const generalErrors = error.response.data.generalErrors;

    // Check if any general error was found.
    if (generalErrors.length > 0) {
      // Modify the error message to contain the first general error.
      error.message = generalErrors[0].message;
    }
  }

  /**
   * Get the custom error message for a given error.
   * @param error
   * @param options
   */
  static getCustomMessage(
    error: EchoError,
    options: CustomErrorOptions
  ): string {
    const customError = this.getCustomError(error, options);

    return customError ? customError.message : error.message;
  }

  /**
   * Get the custom error message for a given error.
   * @param error
   * @param options
   */
  static getCustomDescription(
    error: EchoError,
    options: CustomErrorOptions
  ): string {
    const customError = this.getCustomError(error, options);

    return customError ? customError.description : "";
  }

  /**
   * Get the custom error message for a given error, or undefined when not given.
   * @param error
   * @param options
   */
  private static getCustomError(
    error: EchoError,
    options: CustomErrorOptions
  ): CustomErrorMessage | undefined {
    if (!error) {
      return undefined;
    }

    // Ajust some errors that can be displayed better based on the given error code.
    const customError = this.getCustomErrors(options).find(
      (e) =>
        (error.response &&
          e.code === error.response?.status.toString()) ||
        e.code === error.code
    );

    return customError;
  }

  /**
   * Get a list with custom error messages based on global custom messages & given error options
   * @param options
   */
  private static getCustomErrors(
    options: CustomErrorOptions
  ): Array<CustomErrorMessage> {
    return options.customMessages !== undefined
      ? [...globalCustomErrors, ...options.customMessages]
      : globalCustomErrors;
  }
}
