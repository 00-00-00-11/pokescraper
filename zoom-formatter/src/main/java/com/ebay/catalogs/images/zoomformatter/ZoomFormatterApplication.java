package com.ebay.catalogs.images.zoomformatter;

import org.springframework.boot.Banner.Mode;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.builder.SpringApplicationBuilder;

@SpringBootApplication(exclude={DataSourceAutoConfiguration.class})
public class ZoomFormatterApplication {

  public static void main(String[] args) {
    new SpringApplicationBuilder()
        .sources(ZoomFormatterApplication.class)
        .bannerMode(Mode.OFF)
        .logStartupInfo(false)
        .run(args);

  }

}
