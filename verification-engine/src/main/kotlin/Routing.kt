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
        get("/a") {
            call.respondText("FAAAAHHHH")
        }
    }
}
