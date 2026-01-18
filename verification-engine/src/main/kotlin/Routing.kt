package com.example.com

import io.ktor.server.application.*
import io.ktor.server.response.*
import io.ktor.server.routing.*

fun Application.configureRouting() {
    routing {
        get("/") {
            call.respondText("Hello World! Again")
        }
        get("/hello") {
            call.respondText("This route says hello")
        }
        get("/b") {
            call.respondText("FAAAAHHHH")
        }
        get("/c") {
            call.respondText("YESS")
        }
        get("/d") {
            call.respondText("OKK")
        }
    }
}
