export default {
  namespaced: true,
  state: {
    selectedTheaterId: null,
    selectedDate: null,
    selectedMovie: null,
    scheduleItem: null,

    selectedSeatNumber: null,
    selectedSeatId: null,

    selectedPaymentMethod: null,
  },
  getters: {},
  mutations: {
    SET_SELECTED_THEATER(state, theaterItemId) {
      state.selectedTheaterId = theaterItemId
    },
    SET_SELECTED_DATE(state, dateItem) {
      state.selectedDate = dateItem
    },
    SET_SELECTED_MOVIE(state, movieItem) {
      state.selectedMovie = movieItem
    },
    SET_SELECTED_SCHEDULE(state, scheduleItem) {
      state.scheduleItem = scheduleItem
    },
    SET_SELECTED_SEAT_NO(state, selectedSeatNumber) {
      state.selectedSeatNumber = selectedSeatNumber
    },
    SET_SELECTED_SEAT_ID(state, selectedSeatId) {
      state.selectedSeatId = selectedSeatId
    },
    SET_SELECTED_PAYMENT_METHOD(state, selectedPaymentMethod) {
      state.selectedPaymentMethod = selectedPaymentMethod
    },
    RESET_SELECTED_DATA(state) {
      state.selectedTheaterId = null
      state.selectedDate = null
      state.selectedMovie = null
      state.scheduleItem = null
      state.selectedSeatNumber = null
      state.selectedSeatId = null
      state.selectedPaymentMethod = null
    },
  },
  actions: {},
}
