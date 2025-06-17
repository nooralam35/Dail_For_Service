export function authGuard(user, redirect) {
  if (!user) redirect("/login");
}