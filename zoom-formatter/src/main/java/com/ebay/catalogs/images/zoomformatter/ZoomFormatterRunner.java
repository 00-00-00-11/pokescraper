package com.ebay.catalogs.images.zoomformatter;

import com.ebay.zoom.imageurlbuilder.core.ZoomImageUrlBuilder;
import com.ebay.zoom.imageurlbuilder.util.ImageOptions;
import com.ebay.zoom.imageurlbuilder.util.UrlBuilderResponse;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class ZoomFormatterRunner implements ApplicationRunner {

  @Override
  public void run(ApplicationArguments args) {

    ZoomImageUrlBuilder builder = ZoomImageUrlBuilder.getInstance();
    String url = "http://i.ebayimg.com/00/s/NDAwWDQwMA==/z/k3wAAOSwaNBUcwdk/$_32.JPG";
    ImageOptions options = new ImageOptions(500);
    UrlBuilderResponse response = builder.constructZoomUrl(url, options);
    System.out.println(response.getImageUrl());
    System.exit(0);

  }
}
