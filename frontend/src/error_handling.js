
export function check_errors(errors, fieldname) {
  if (errors === null) return "";
  for (const error of errors) {
    if (error.field === fieldname) {
      return error.message;
    }
  }
  return "";
}


export async function get_errors(error) {
  return error.json ? await error.json().then(res => res.errors).catch(() => null) : null;
}
