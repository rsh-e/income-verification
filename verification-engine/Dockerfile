FROM amazoncorretto:17

WORKDIR /src

COPY build/libs/verification-engine-all.jar app.jar

EXPOSE 8081

ENTRYPOINT [ "java", "-jar", "app.jar" ]