import {EchoError} from 'echofetch';
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
    code: "403",
    message: "Geen toegang",
    description:
      "Je hebt onvoldoende rechten om deze actie uit te voeren",
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
  static async handle(
    error: EchoError,
    options: CustomErrorOptions,
    fields: InputFields = {}
  ) {
    let errors = error.json ? await error.json().catch(() => null) : null;

    // Handle field errors.
    this.handleInputFields(error, fields)

    // Handle general errors.
    this.handleGeneral(error, errors)

    // Emit the error on the ErrorBus.
    emitter.emit("error", error, options)

    // Clear the error when navigating to a different route.
    router.afterEach(() => {
      emitter.emit("error-clear")
    });

  }

  /**
   * Handle the error for the given InputFields.
   * This will add an error to every given field with errors.
   * @param errors
   * @param fields
   */
  static handleInputFields(errors: any, fields: InputFields) {
    // Check if the input errors are undefined.
    if (!errors) {
      return;
    }

    // Set the error messages for every field.
    for (const fieldName of Object.keys(fields)) {
      const fieldValue = fields[fieldName];
      const fieldNewError = errors.find(
        (inputError: InputFieldError) => inputError.field === fieldName
      );

      // Set the new error message, when available.
      if (fieldNewError) {
        fieldValue.error = fieldNewError.message;
      } else { // Otherwise set an empty error. (necessary for reset of previous error)
        fieldValue.error = "";
      }
    }
  }

  /**
   * Handle general errors.
   * This will modify the error to the first given "generalError" message
   * @param error
   * @param errors
   */
  static handleGeneral(error: EchoError, errors: any) {
    error.message = this.getCustomMessage(error, new CustomErrorOptions()); // (temp?) fix
    // Check if the general errors are undefined.
    if (!errors || !errors.errors) {
      return;
    }

    const generalErrors = errors.errors

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
      e =>
        (error.status &&
          e.code === error.status.toString())
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
