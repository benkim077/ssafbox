import Vue from "vue"
import VueRouter from "vue-router"
import IndexView from "@/views/Index/IndexView"
import SignUpView from "@/views/Auth/SignUpView"
import LoginView from "@/views/Auth/LoginView"
import AdminView from "@/views/Admin/AdminView"
import AdminTheaterView from "@/views/Admin/AdminTheaterView"
import AdminTheaterManageView from "@/views/Admin/AdminTheaterManageView"
import AdminScreenManageView from "@/views/Admin/AdminScreenManageView"
import TicketView from "@/views/Ticket/TicketView"
import TicketSelectScheduleView from "@/views/Ticket/TicketSelectScheduleView"
import TicketSelectSeatView from "@/views/Ticket/TicketSelectSeatView"
import PaymentView from "@/views/Ticket/Payment/PaymentView"
import PaymentCompleteView from "@/views/Ticket/Payment/PaymentCompleteView"
import CheckTicketView from "@/views/CheckTicket/CheckTicketView"

Vue.use(VueRouter)

const routes = [
  {
    path: "/index",
    name: "index",
    component: IndexView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUpView,
  },
  {
    path: "/ticket/payment/:uuid/success",
    name: "paymentComplete",
    components: {
      default: PaymentCompleteView,
    },
  },
  {
    path: "/ticket",
    name: "ticket",
    component: TicketView,
    children: [
      //
      {
        path: "schedules",
        name: "schedules",
        component: TicketSelectScheduleView,
      },
      {
        path: "seat",
        name: "seat",
        component: TicketSelectSeatView,
      },
      {
        path: "payment",
        name: "payment",
        component: PaymentView,
      },
    ],
  },
  {
    path: "/check",
    name: "check",
    component: CheckTicketView,
  },
  {
    path: "/admin",
    name: "admin",
    component: AdminView,
    children: [
      {
        path: "theater",
        name: "adminTheater",
        component: AdminTheaterView,
      },
      {
        path: "theater/:theaterId",
        name: "manageTheater",
        component: AdminTheaterManageView,
      },
      {
        path: "/admin/theater/:theaterId/:screenId",
        name: "manageScreen",
        component: AdminScreenManageView,
      },
    ],
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
