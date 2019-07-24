package com.ebay.catalogs.images.zoomformatter.mediarepo.accessor;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class Page {

  private int offset;

  private int limit;

}
