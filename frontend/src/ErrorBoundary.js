import React from "react";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    // Update state so next render shows fallback UI
    return { hasError: true, error };
  }

  componentDidCatch(error, info) {
    // You can log the error to a service
    console.error("Error Boundary caught:", error, info);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ color: "red" }}>
          <h2>Something went wrong.</h2>
          <p>{this.state.error.toString()}</p>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
