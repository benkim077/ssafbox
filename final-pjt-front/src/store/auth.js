import http from "@/api/http"
import router from "@/router/index"
export default {
  namespaced: true,
  state: {
    accessToken: null,
    refreshToken: null,
    userId: null,
    isStaff: false,
  },
  getters: {
    isLoggedIn(state) {
      return state.accessToken && state.refreshToken ? true : false
    },
  },
  mutations: {
    SET_ACCESS_TOKEN(state, accessToken) {
      state.accessToken = accessToken
    },
    SET_REFRESH_TOKEN(state, refreshToken) {
      state.refreshToken = refreshToken
    },
    DELETE_ACCESS_TOKEN(state) {
      state.accessToken = null
    },
    DELETE_REFRESH_TOKEN(state) {
      state.refreshToken = null
    },
    SET_USER_ID(state, userId) {
      state.userId = userId
    },
    SET_IS_STAFF(state, isStaff) {
      state.isStaff = isStaff
    },
  },
  actions: {
    async refreshAccessToken(context) {
      return http({
        method: "post",
        url: `/api/accounts/token/refresh/`,
        data: {
          refresh: context.state.refreshToken,
        },
      })
        .then((res) => {
          context.commit("SET_ACCESS_TOKEN", res.data.access)
        })
        .catch((err) => {
          console.log(err)
          router.push({ name: "login" })
        })
    },
  },
}
