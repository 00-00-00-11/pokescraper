package com.ebay.catalogs.images.zoomformatter.model;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class MediaRepoBO {

  private long id;
  private String ebayUrl;
  private String md5;
  private String providerId;
  private Integer width;
  private Integer height;
  private String copyright;
  private String subCopyright;
  private String sourceUrl;
  private String analysisData;

}
