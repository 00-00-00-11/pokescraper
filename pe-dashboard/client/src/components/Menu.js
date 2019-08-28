import React from "react";
import ButtonToolbar from "react-bootstrap/ButtonToolbar";
import Button from "react-bootstrap/Button";

var imageStyle = {
  width: '50%'
};

export default class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      product: props.product,
    };

  }

  render() {
    return (
        <div>
          <div className={"SearchAndLogoContainer"}>
            <div className={"BigTitle"}>Welcome to PE dashboard</div>
            <div><h2>select a task</h2></div>
          <ButtonToolbar>
            <Button variant="success" size="lg">Resend</Button>
            <Button variant="success" size="lg">Reprocess</Button>
            <Button variant="success" size="lg">Track source</Button>
            <Button variant="success" size="lg">Browse tables</Button>
            <Button variant="success" size="lg">Track Sources</Button>
          </ButtonToolbar>
        </div>
        </div>

    );

  }

}