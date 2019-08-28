const request = require('request');
var express = require('express');
const rp = require('request-promise');

var router = express.Router();

router.get('/epid/:epid', function (req, res, next) {
  trackByEpid(req, function (body) {
    res.json(body);
  });

});

router.get('/details/:details', function (req, res, next) {
  trackByDetails(req, function (body) {
    res.json(body);
  });
});

function trackByEpid(req, callback) {
  request(
      'http://petracker.qa.ebay.com/petrack2/internal/findAggregationMappingByEpid/'
      + req.params.epid + '?&mode=verbose', {json: true},
      (err, res, body) => {
        if (err) {
          return err;
        }
        callback(body);
      });
}

function trackByDetails(req, callback) {
  request(
      'http://petrack2.stratus.ebay.com/petrack2/internal/itemTrackingDetailsByRawKey/'
      + req.params.details + '?mode=verbose', {json: true},
      (err, res, body) => {
        if (err) {
          return err;
        }
        callback(body);
      });
}

module.exports = router;

