import http from "./http"
import store from "@/store"

export async function login(username, password) {
  const response = await http({
    method: "post",
    url: "/api/accounts/login/",
    data: {
      username,
      password,
    },
  })

  if (response.status === 200) {
    store.commit("auth/SET_ACCESS_TOKEN", response.data.access_token)
    store.commit("auth/SET_REFRESH_TOKEN", response.data.refresh_token)
    store.commit("auth/SET_USER_ID", response.data.user.id)
    store.commit("auth/SET_IS_STAFF", response.data.is_staff)
  }

  return response
}

export async function signup(username, password1, password2) {
  const response = await http({
    method: "post",
    url: "/api/accounts/register/",
    data: {
      username,
      password1,
      password2,
    },
  })

  if (response.status === 201) {
    store.commit("auth/SET_ACCESS_TOKEN", response.data.access_token)
    store.commit("auth/SET_REFRESH_TOKEN", response.data.refresh_token)
  }

  return response
}
