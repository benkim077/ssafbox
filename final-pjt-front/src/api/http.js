import axios from "axios"
import store from "@/store"
import serverURL from "./backend"

const instance = axios.create({
  baseURL: serverURL,
})

instance.interceptors.request.use(function (config) {
  if (
    (instance.url !== "/api/accounts/login" ||
      instance.url !== "api/accounts/register/") &&
    store.state.auth.accessToken !== null
  ) {
    config["headers"] = {
      Authorization: `Bearer ${store.state.auth.accessToken}`,
    }
  }
  return config
})

instance.interceptors.response.use(
  function (res) {
    return res
  },
  async function (err) {
    const { config } = err

    if (err.response.data.code === "token_not_valid") {
      const originalRequest = config
      await store.dispatch("auth/refreshAccessToken")

      originalRequest.headers.authorization = `Bearer ${store.state.auth.accessToken}`
      return instance(originalRequest)
    }

    return Promise.reject(err)
  }
)

export default instance
