import http from "./http"

export async function getReservedTicketList() {
  return await http({
    method: "get",
    url: `/api/user-reserved-seats/`,
  })
}
