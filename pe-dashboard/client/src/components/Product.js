import React from "react";
import {Col, Container, Row,Nav} from "react-bootstrap";
import Image from "react-bootstrap/Image";

var imageStyle = {
  width: '50%'
};

export default class Product extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      product: props.product,
    };


  }

  render() {
    const {product} = this.state;
    return (
        <div>
          <Container>
            <Row>
              <Col sm={"auto"}>
                <Image style={imageStyle} src="" />
              </Col>
              <Col  sm={"auto"}>
                <Nav.Link href="">title</Nav.Link>
              </Col>
            </Row>
          </Container>
        </div>

    );

  }

}