package com.ebay.catalogs.r12npecomperator;

import com.ebay.catalogs.r12npecomperator.pojo.ComparissonSummeryResult;
import com.ebay.catalogs.r12npecomperator.process.ComparisionProcessor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class R12NPeComparatorRunner implements ApplicationRunner {

  private static final Logger logger = LoggerFactory.getLogger(R12NPeComparatorRunner.class);

  private final ComparisionProcessor comparisionProcessor;

  public R12NPeComparatorRunner(ComparisionProcessor comparisionProcessor) {
    this.comparisionProcessor = comparisionProcessor;
  }

  @Override
  public void run(ApplicationArguments args) throws Exception {
    logger.info("Starting conversion");
    ComparissonSummeryResult comparissonSummeryResult = comparisionProcessor.compare();
    logger.info("Done comparing epids, files are saved to: " + comparissonSummeryResult.getOutputFileFullPathName());
    logger.info("Compared : " + comparissonSummeryResult.getNumberOfConvertedEpids() + " epids");
    logger.info("Didn't Compare : " + comparissonSummeryResult.getNumberOfFailedEpids() + " epids");
    System.exit(0);
  }
}
