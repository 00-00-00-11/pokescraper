package com.ebay.catalogs.r12npecomperator.process;

import com.ebay.catalogs.r12npecomperator.pojo.ComparissonSummeryResult;
import org.springframework.stereotype.Component;

@Component
public class ComparisionProcessor {

  public ComparissonSummeryResult compare(){
    return ComparissonSummeryResult.builder().build();
  }

}
