import http from "./http"

export async function createTheater(name, location) {
  return await http({
    method: "post",
    url: "/api/theaters/",
    data: {
      name,
      location,
    },
  })
}

export async function readTheaterList() {
  return await http({
    method: "get",
    url: "/api/theaters/",
  })
}

export async function readTheaterItem(id) {
  return await http({
    method: "get",
    url: `/api/theaters/${id}/`,
  })
}

export async function updateTheaterItem(id, name, location) {
  return await http({
    method: "patch",
    url: `/api/theaters/${id}/`,
    data: {
      name,
      location,
    },
  })
}

export async function deleteTheaterItem(id) {
  return await http({
    method: "delete",
    url: `/api/theaters/${id}/`,
  })
}

export async function getScreenList(theater_pk) {
  return await http({
    method: "get",
    url: `/api/theaters/${theater_pk}/screens/`,
  })
}

export async function createScreen(theater_pk, seats) {
  return await http({
    method: "post",
    url: `/api/theaters/${theater_pk}/screens/`,
    data: {
      seats,
    },
  })
}

export async function getScreenItem(theater_pk, id) {
  return await http({
    method: "get",
    url: `/api/theaters/${theater_pk}/screens/${id}/`,
  })
}

export async function updateScreenItem(theater_pk, id, seats) {
  return await http({
    method: "patch",
    url: `/api/theaters/${theater_pk}/screens/${id}/`,
    data: {
      seats,
    },
  })
}

export async function deleteScreenItem(theater_pk, id) {
  return await http({
    method: "delete",
    url: `/api/theaters/${theater_pk}/screens/${id}/`,
  })
}

export async function createSchedule(
  theater_pk,
  screen_pk,
  start_date,
  start_time,
  movie
) {
  return await http({
    method: "post",
    url: `/api/theaters/${theater_pk}/screens/${screen_pk}/schedules/`,
    data: {
      start_date,
      start_time,
      movie,
    },
  })
}

export async function getScheduleList(theater_pk, screen_pk) {
  return await http({
    method: "get",
    url: `/api/theaters/${theater_pk}/screens/${screen_pk}/schedules/`,
  })
}

export async function getScheduleItem(theater_pk, screen_pk, id) {
  return await http({
    method: "get",
    url: `/api/theaters/${theater_pk}/screens/${screen_pk}/schedules/${id}/`,
  })
}

export async function updateScheduleItem(
  theater_pk,
  screen_pk,
  id,
  start_date,
  start_time,
  movie
) {
  return await http({
    method: "patch",
    url: `/api/theaters/${theater_pk}/screens/${screen_pk}/schedules/${id}/`,
    data: {
      start_date,
      start_time,
      movie,
    },
  })
}

export async function deleteScheduleItem(theater_pk, screen_pk, id) {
  return await http({
    method: "delete",
    url: `/api/theaters/${theater_pk}/screens/${screen_pk}/schedules/${id}/`,
  })
}
