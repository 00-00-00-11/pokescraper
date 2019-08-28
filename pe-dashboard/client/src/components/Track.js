import React from "react";
import {Button, Col, Container, Form, Row} from "react-bootstrap";

var imageStyle = {
  width: '50%'
};

var codeStyle = {
  margin: '20px'
};

export default class Track extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
      epid: props.epid,
      trackDetails: null
    };

    this.findByEpid = this.findByEpid.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }


  handleChange(event) {
    event.preventDefault()
    this.setState({epid: event.target.value});
  };

  findByEpid() {
    fetch("/tracker/epid/" + this.state.epid,
        {
          method: "GET",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }
        })
    .then(res => res.json())
    .then(
        (result) => {
          this.setState({
            isLoaded: true,
            trackDetails: result,
            epid:this.state.epid
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
    )
  }

  render() {
    const { epid, trackDetails} = this.state;
 /*   if(trackDetails && !trackDetails[0].found){
      return <h1>NOT FOUND</h1>
    }*/
    return (

        <div>
          <Form inline="true">
            <input
                style={codeStyle}
                type="text"
                name="epid"
                value={epid}
                onChange={this.handleChange}
            />
            <Button onClick={this.findByEpid}
                    variant="outline-info">Find</Button>
          </Form>
          {
            trackDetails &&  trackDetails.map(detail => (
                <div>
                  <Container>
                    <Row>
                      <Col>
                        <p>aggregationKey {detail.aggregationKey}</p>
                      </Col>
                    </Row>
                  </Container>
                </div>
            ))
          }
        </div>
    );

  }

}