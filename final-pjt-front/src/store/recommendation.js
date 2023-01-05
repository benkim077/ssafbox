export default {
  namespaced: true,
  state: {
    movieId: null,
  },
  getters: {},
  mutations: {
    SET_RECOMMENDED_MOVIE(state, movieId) {
      state.movieId = movieId
    },
  },
  actions: {},
}
