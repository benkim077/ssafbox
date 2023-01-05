export default {
  namespaced: true,
  state: {
    theaterId: null,
    screenId: null,
    theaterList: [],
    screenList: [],
    scheduleList: [],
  },
  getters: {
    getTheaterList(state) {
      return state.theaterList
    },
    getScreenList(state) {
      return state.screenList
    },
    getScheduleList(state) {
      return state.scheduleList
    },
  },
  mutations: {
    STORE_THEATER_ID(state, theaterId) {
      state.theaterId = theaterId
    },
    STORE_SCREEN_ID(state, screenId) {
      state.screenId = screenId
    },
    SET_THEATER_LIST(state, theaterList) {
      state.theaterList = theaterList
    },
    SET_SCREEN_LIST(state, screenList) {
      state.screenList = screenList
    },
    SET_SCHEDULE_LIST(state, scheduleList) {
      state.scheduleList = scheduleList
    },
    PUSH_THEATER_ITEM(state, theaterItem) {
      state.theaterList.push(theaterItem)
    },
    PUSH_SCREEN_ITEM(state, screenItem) {
      state.screenList.push(screenItem)
    },
    PUSH_SCHEDULE_ITEM(state, scheduleItem) {
      state.scheduleList.push(scheduleItem)
    },
    DELETE_SCHEDULE_ITEM(state, scheduleItem) {
      state.scheduleList.splice(state.scheduleList.indexOf(scheduleItem), 1)
    },
  },
  actions: {},
}
